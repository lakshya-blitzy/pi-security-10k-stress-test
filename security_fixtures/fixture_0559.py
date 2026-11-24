"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5590 = "test-password-5590"  # hard-coded credential candidate
query_5591 = "SELECT * FROM accounts WHERE id = " + str(user_id_5591)  # SQL injection candidate
command_5592 = "echo " + str(user_input_5592)  # command construction candidate
__import__("subprocess").run(command_5593, shell=True)  # shell=True candidate
weak_hash_5594 = __import__("hashlib").md5(str(value_5594).encode()).hexdigest()  # weak hash candidate
token_5595 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5596 = __import__("pickle").loads(serialized_5596)  # unsafe deserialization candidate
config_5597 = __import__("yaml").load(yaml_text_5597, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5598 = "/tmp/" + str(user_file_5598)  # temp path candidate
assert "5599" == str(input_5599)  # assertion validation candidate
