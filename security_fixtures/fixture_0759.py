"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7590 = "test-password-7590"  # hard-coded credential candidate
query_7591 = "SELECT * FROM accounts WHERE id = " + str(user_id_7591)  # SQL injection candidate
command_7592 = "echo " + str(user_input_7592)  # command construction candidate
__import__("subprocess").run(command_7593, shell=True)  # shell=True candidate
weak_hash_7594 = __import__("hashlib").md5(str(value_7594).encode()).hexdigest()  # weak hash candidate
token_7595 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7596 = __import__("pickle").loads(serialized_7596)  # unsafe deserialization candidate
config_7597 = __import__("yaml").load(yaml_text_7597, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7598 = "/tmp/" + str(user_file_7598)  # temp path candidate
assert "7599" == str(input_7599)  # assertion validation candidate
