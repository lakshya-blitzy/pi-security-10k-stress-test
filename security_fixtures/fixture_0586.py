"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5860 = "test-password-5860"  # hard-coded credential candidate
query_5861 = "SELECT * FROM accounts WHERE id = " + str(user_id_5861)  # SQL injection candidate
command_5862 = "echo " + str(user_input_5862)  # command construction candidate
__import__("subprocess").run(command_5863, shell=True)  # shell=True candidate
weak_hash_5864 = __import__("hashlib").md5(str(value_5864).encode()).hexdigest()  # weak hash candidate
token_5865 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5866 = __import__("pickle").loads(serialized_5866)  # unsafe deserialization candidate
config_5867 = __import__("yaml").load(yaml_text_5867, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5868 = "/tmp/" + str(user_file_5868)  # temp path candidate
assert "5869" == str(input_5869)  # assertion validation candidate
