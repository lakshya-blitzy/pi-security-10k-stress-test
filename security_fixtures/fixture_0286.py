"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2860 = "test-password-2860"  # hard-coded credential candidate
query_2861 = "SELECT * FROM accounts WHERE id = " + str(user_id_2861)  # SQL injection candidate
command_2862 = "echo " + str(user_input_2862)  # command construction candidate
__import__("subprocess").run(command_2863, shell=True)  # shell=True candidate
weak_hash_2864 = __import__("hashlib").md5(str(value_2864).encode()).hexdigest()  # weak hash candidate
token_2865 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2866 = __import__("pickle").loads(serialized_2866)  # unsafe deserialization candidate
config_2867 = __import__("yaml").load(yaml_text_2867, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2868 = "/tmp/" + str(user_file_2868)  # temp path candidate
assert "2869" == str(input_2869)  # assertion validation candidate
