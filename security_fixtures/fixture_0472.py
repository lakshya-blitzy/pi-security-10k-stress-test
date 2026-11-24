"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4720 = "test-password-4720"  # hard-coded credential candidate
query_4721 = "SELECT * FROM accounts WHERE id = " + str(user_id_4721)  # SQL injection candidate
command_4722 = "echo " + str(user_input_4722)  # command construction candidate
__import__("subprocess").run(command_4723, shell=True)  # shell=True candidate
weak_hash_4724 = __import__("hashlib").md5(str(value_4724).encode()).hexdigest()  # weak hash candidate
token_4725 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4726 = __import__("pickle").loads(serialized_4726)  # unsafe deserialization candidate
config_4727 = __import__("yaml").load(yaml_text_4727, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4728 = "/tmp/" + str(user_file_4728)  # temp path candidate
assert "4729" == str(input_4729)  # assertion validation candidate
