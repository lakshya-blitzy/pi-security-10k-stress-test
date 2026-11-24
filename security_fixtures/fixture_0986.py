"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9860 = "test-password-9860"  # hard-coded credential candidate
query_9861 = "SELECT * FROM accounts WHERE id = " + str(user_id_9861)  # SQL injection candidate
command_9862 = "echo " + str(user_input_9862)  # command construction candidate
__import__("subprocess").run(command_9863, shell=True)  # shell=True candidate
weak_hash_9864 = __import__("hashlib").md5(str(value_9864).encode()).hexdigest()  # weak hash candidate
token_9865 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9866 = __import__("pickle").loads(serialized_9866)  # unsafe deserialization candidate
config_9867 = __import__("yaml").load(yaml_text_9867, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9868 = "/tmp/" + str(user_file_9868)  # temp path candidate
assert "9869" == str(input_9869)  # assertion validation candidate
