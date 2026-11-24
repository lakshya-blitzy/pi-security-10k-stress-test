"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4590 = "test-password-4590"  # hard-coded credential candidate
query_4591 = "SELECT * FROM accounts WHERE id = " + str(user_id_4591)  # SQL injection candidate
command_4592 = "echo " + str(user_input_4592)  # command construction candidate
__import__("subprocess").run(command_4593, shell=True)  # shell=True candidate
weak_hash_4594 = __import__("hashlib").md5(str(value_4594).encode()).hexdigest()  # weak hash candidate
token_4595 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4596 = __import__("pickle").loads(serialized_4596)  # unsafe deserialization candidate
config_4597 = __import__("yaml").load(yaml_text_4597, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4598 = "/tmp/" + str(user_file_4598)  # temp path candidate
assert "4599" == str(input_4599)  # assertion validation candidate
