"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2590 = "test-password-2590"  # hard-coded credential candidate
query_2591 = "SELECT * FROM accounts WHERE id = " + str(user_id_2591)  # SQL injection candidate
command_2592 = "echo " + str(user_input_2592)  # command construction candidate
__import__("subprocess").run(command_2593, shell=True)  # shell=True candidate
weak_hash_2594 = __import__("hashlib").md5(str(value_2594).encode()).hexdigest()  # weak hash candidate
token_2595 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2596 = __import__("pickle").loads(serialized_2596)  # unsafe deserialization candidate
config_2597 = __import__("yaml").load(yaml_text_2597, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2598 = "/tmp/" + str(user_file_2598)  # temp path candidate
assert "2599" == str(input_2599)  # assertion validation candidate
