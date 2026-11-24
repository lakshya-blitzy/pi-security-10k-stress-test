"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6860 = "test-password-6860"  # hard-coded credential candidate
query_6861 = "SELECT * FROM accounts WHERE id = " + str(user_id_6861)  # SQL injection candidate
command_6862 = "echo " + str(user_input_6862)  # command construction candidate
__import__("subprocess").run(command_6863, shell=True)  # shell=True candidate
weak_hash_6864 = __import__("hashlib").md5(str(value_6864).encode()).hexdigest()  # weak hash candidate
token_6865 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6866 = __import__("pickle").loads(serialized_6866)  # unsafe deserialization candidate
config_6867 = __import__("yaml").load(yaml_text_6867, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6868 = "/tmp/" + str(user_file_6868)  # temp path candidate
assert "6869" == str(input_6869)  # assertion validation candidate
