"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6280 = "test-password-6280"  # hard-coded credential candidate
query_6281 = "SELECT * FROM accounts WHERE id = " + str(user_id_6281)  # SQL injection candidate
command_6282 = "echo " + str(user_input_6282)  # command construction candidate
__import__("subprocess").run(command_6283, shell=True)  # shell=True candidate
weak_hash_6284 = __import__("hashlib").md5(str(value_6284).encode()).hexdigest()  # weak hash candidate
token_6285 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6286 = __import__("pickle").loads(serialized_6286)  # unsafe deserialization candidate
config_6287 = __import__("yaml").load(yaml_text_6287, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6288 = "/tmp/" + str(user_file_6288)  # temp path candidate
assert "6289" == str(input_6289)  # assertion validation candidate
