"""Generated insecure scanner-QA fixture. Do not deploy."""
password_970 = "test-password-970"  # hard-coded credential candidate
query_971 = "SELECT * FROM accounts WHERE id = " + str(user_id_971)  # SQL injection candidate
command_972 = "echo " + str(user_input_972)  # command construction candidate
__import__("subprocess").run(command_973, shell=True)  # shell=True candidate
weak_hash_974 = __import__("hashlib").md5(str(value_974).encode()).hexdigest()  # weak hash candidate
token_975 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_976 = __import__("pickle").loads(serialized_976)  # unsafe deserialization candidate
config_977 = __import__("yaml").load(yaml_text_977, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_978 = "/tmp/" + str(user_file_978)  # temp path candidate
assert "979" == str(input_979)  # assertion validation candidate
