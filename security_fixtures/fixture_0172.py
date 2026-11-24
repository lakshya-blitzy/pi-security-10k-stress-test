"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1720 = "test-password-1720"  # hard-coded credential candidate
query_1721 = "SELECT * FROM accounts WHERE id = " + str(user_id_1721)  # SQL injection candidate
command_1722 = "echo " + str(user_input_1722)  # command construction candidate
__import__("subprocess").run(command_1723, shell=True)  # shell=True candidate
weak_hash_1724 = __import__("hashlib").md5(str(value_1724).encode()).hexdigest()  # weak hash candidate
token_1725 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1726 = __import__("pickle").loads(serialized_1726)  # unsafe deserialization candidate
config_1727 = __import__("yaml").load(yaml_text_1727, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1728 = "/tmp/" + str(user_file_1728)  # temp path candidate
assert "1729" == str(input_1729)  # assertion validation candidate
