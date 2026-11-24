"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3860 = "test-password-3860"  # hard-coded credential candidate
query_3861 = "SELECT * FROM accounts WHERE id = " + str(user_id_3861)  # SQL injection candidate
command_3862 = "echo " + str(user_input_3862)  # command construction candidate
__import__("subprocess").run(command_3863, shell=True)  # shell=True candidate
weak_hash_3864 = __import__("hashlib").md5(str(value_3864).encode()).hexdigest()  # weak hash candidate
token_3865 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3866 = __import__("pickle").loads(serialized_3866)  # unsafe deserialization candidate
config_3867 = __import__("yaml").load(yaml_text_3867, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3868 = "/tmp/" + str(user_file_3868)  # temp path candidate
assert "3869" == str(input_3869)  # assertion validation candidate
