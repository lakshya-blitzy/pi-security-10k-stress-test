"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7860 = "test-password-7860"  # hard-coded credential candidate
query_7861 = "SELECT * FROM accounts WHERE id = " + str(user_id_7861)  # SQL injection candidate
command_7862 = "echo " + str(user_input_7862)  # command construction candidate
__import__("subprocess").run(command_7863, shell=True)  # shell=True candidate
weak_hash_7864 = __import__("hashlib").md5(str(value_7864).encode()).hexdigest()  # weak hash candidate
token_7865 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7866 = __import__("pickle").loads(serialized_7866)  # unsafe deserialization candidate
config_7867 = __import__("yaml").load(yaml_text_7867, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7868 = "/tmp/" + str(user_file_7868)  # temp path candidate
assert "7869" == str(input_7869)  # assertion validation candidate
