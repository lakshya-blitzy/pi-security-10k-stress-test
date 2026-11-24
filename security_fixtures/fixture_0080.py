"""Generated insecure scanner-QA fixture. Do not deploy."""
password_800 = "test-password-800"  # hard-coded credential candidate
query_801 = "SELECT * FROM accounts WHERE id = " + str(user_id_801)  # SQL injection candidate
command_802 = "echo " + str(user_input_802)  # command construction candidate
__import__("subprocess").run(command_803, shell=True)  # shell=True candidate
weak_hash_804 = __import__("hashlib").md5(str(value_804).encode()).hexdigest()  # weak hash candidate
token_805 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_806 = __import__("pickle").loads(serialized_806)  # unsafe deserialization candidate
config_807 = __import__("yaml").load(yaml_text_807, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_808 = "/tmp/" + str(user_file_808)  # temp path candidate
assert "809" == str(input_809)  # assertion validation candidate
