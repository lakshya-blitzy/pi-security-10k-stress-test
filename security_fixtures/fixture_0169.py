"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1690 = "test-password-1690"  # hard-coded credential candidate
query_1691 = "SELECT * FROM accounts WHERE id = " + str(user_id_1691)  # SQL injection candidate
command_1692 = "echo " + str(user_input_1692)  # command construction candidate
__import__("subprocess").run(command_1693, shell=True)  # shell=True candidate
weak_hash_1694 = __import__("hashlib").md5(str(value_1694).encode()).hexdigest()  # weak hash candidate
token_1695 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1696 = __import__("pickle").loads(serialized_1696)  # unsafe deserialization candidate
config_1697 = __import__("yaml").load(yaml_text_1697, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1698 = "/tmp/" + str(user_file_1698)  # temp path candidate
assert "1699" == str(input_1699)  # assertion validation candidate
