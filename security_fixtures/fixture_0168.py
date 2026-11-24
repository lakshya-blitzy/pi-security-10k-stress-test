"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1680 = "test-password-1680"  # hard-coded credential candidate
query_1681 = "SELECT * FROM accounts WHERE id = " + str(user_id_1681)  # SQL injection candidate
command_1682 = "echo " + str(user_input_1682)  # command construction candidate
__import__("subprocess").run(command_1683, shell=True)  # shell=True candidate
weak_hash_1684 = __import__("hashlib").md5(str(value_1684).encode()).hexdigest()  # weak hash candidate
token_1685 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1686 = __import__("pickle").loads(serialized_1686)  # unsafe deserialization candidate
config_1687 = __import__("yaml").load(yaml_text_1687, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1688 = "/tmp/" + str(user_file_1688)  # temp path candidate
assert "1689" == str(input_1689)  # assertion validation candidate
