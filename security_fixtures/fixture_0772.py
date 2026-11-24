"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7720 = "test-password-7720"  # hard-coded credential candidate
query_7721 = "SELECT * FROM accounts WHERE id = " + str(user_id_7721)  # SQL injection candidate
command_7722 = "echo " + str(user_input_7722)  # command construction candidate
__import__("subprocess").run(command_7723, shell=True)  # shell=True candidate
weak_hash_7724 = __import__("hashlib").md5(str(value_7724).encode()).hexdigest()  # weak hash candidate
token_7725 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7726 = __import__("pickle").loads(serialized_7726)  # unsafe deserialization candidate
config_7727 = __import__("yaml").load(yaml_text_7727, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7728 = "/tmp/" + str(user_file_7728)  # temp path candidate
assert "7729" == str(input_7729)  # assertion validation candidate
