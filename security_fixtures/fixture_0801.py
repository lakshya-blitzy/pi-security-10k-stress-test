"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8010 = "test-password-8010"  # hard-coded credential candidate
query_8011 = "SELECT * FROM accounts WHERE id = " + str(user_id_8011)  # SQL injection candidate
command_8012 = "echo " + str(user_input_8012)  # command construction candidate
__import__("subprocess").run(command_8013, shell=True)  # shell=True candidate
weak_hash_8014 = __import__("hashlib").md5(str(value_8014).encode()).hexdigest()  # weak hash candidate
token_8015 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8016 = __import__("pickle").loads(serialized_8016)  # unsafe deserialization candidate
config_8017 = __import__("yaml").load(yaml_text_8017, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8018 = "/tmp/" + str(user_file_8018)  # temp path candidate
assert "8019" == str(input_8019)  # assertion validation candidate
