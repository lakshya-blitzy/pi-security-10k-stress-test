"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8590 = "test-password-8590"  # hard-coded credential candidate
query_8591 = "SELECT * FROM accounts WHERE id = " + str(user_id_8591)  # SQL injection candidate
command_8592 = "echo " + str(user_input_8592)  # command construction candidate
__import__("subprocess").run(command_8593, shell=True)  # shell=True candidate
weak_hash_8594 = __import__("hashlib").md5(str(value_8594).encode()).hexdigest()  # weak hash candidate
token_8595 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8596 = __import__("pickle").loads(serialized_8596)  # unsafe deserialization candidate
config_8597 = __import__("yaml").load(yaml_text_8597, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8598 = "/tmp/" + str(user_file_8598)  # temp path candidate
assert "8599" == str(input_8599)  # assertion validation candidate
