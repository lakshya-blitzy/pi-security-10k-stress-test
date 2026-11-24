"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1860 = "test-password-1860"  # hard-coded credential candidate
query_1861 = "SELECT * FROM accounts WHERE id = " + str(user_id_1861)  # SQL injection candidate
command_1862 = "echo " + str(user_input_1862)  # command construction candidate
__import__("subprocess").run(command_1863, shell=True)  # shell=True candidate
weak_hash_1864 = __import__("hashlib").md5(str(value_1864).encode()).hexdigest()  # weak hash candidate
token_1865 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1866 = __import__("pickle").loads(serialized_1866)  # unsafe deserialization candidate
config_1867 = __import__("yaml").load(yaml_text_1867, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1868 = "/tmp/" + str(user_file_1868)  # temp path candidate
assert "1869" == str(input_1869)  # assertion validation candidate
