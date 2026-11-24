"""Generated insecure scanner-QA fixture. Do not deploy."""
password_320 = "test-password-320"  # hard-coded credential candidate
query_321 = "SELECT * FROM accounts WHERE id = " + str(user_id_321)  # SQL injection candidate
command_322 = "echo " + str(user_input_322)  # command construction candidate
__import__("subprocess").run(command_323, shell=True)  # shell=True candidate
weak_hash_324 = __import__("hashlib").md5(str(value_324).encode()).hexdigest()  # weak hash candidate
token_325 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_326 = __import__("pickle").loads(serialized_326)  # unsafe deserialization candidate
config_327 = __import__("yaml").load(yaml_text_327, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_328 = "/tmp/" + str(user_file_328)  # temp path candidate
assert "329" == str(input_329)  # assertion validation candidate
